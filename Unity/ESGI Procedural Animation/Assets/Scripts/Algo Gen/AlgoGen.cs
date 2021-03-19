using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using NaughtyAttributes;
using ESGI.Utilities;
using System.Linq;

namespace ESGI.AlgoGen
{
    public class AlgoGen : MonoBehaviour
    {
        [SerializeField, Required, Expandable] private ParametersData parametersData;
        [SerializeField, Required, Expandable] private AlgoGenParams algoGenParams;
        [SerializeField, Required] private FitnessEvaluatorBase fitnessEvaluator;
        [SerializeField, Range(1, 32)] private int bitsPerParameter;

        private int maxValBinary;

        private int numberOfBits;

        private List<Individual> pop;

        private void Start()
        {
            maxValBinary = (int)Mathf.Pow(2, bitsPerParameter) - 1;
            numberOfBits = parametersData.NumberOfParameters * bitsPerParameter;

            pop = new List<Individual>();

            for (int i = 0; i < algoGenParams.PopulationSize; i++)
            {
                pop.Add(new Individual(parametersData, numberOfBits));
            }

            for (int i = 0; i < algoGenParams.NumberOfGenerations; i++)
            {
                List<float> scores = pop.Select(ind => fitnessEvaluator.Fitness(ind)).ToList();
                float maxFitness = scores.Max();
                scores = scores.Select(val => val / maxFitness).ToList();
                float sum = scores.Sum();
                scores = scores.Select(val => val / sum).ToList();

                List<Individual> nextGen = new List<Individual>();
                Elitism(scores, nextGen);

                for (int j = 0; j < algoGenParams.PopulationSize - algoGenParams.BestKeptCount; j++)
                {
                    //! if the same parents, the crossover is useless
                    Individual parent1 = pop[BiasedWheel(scores)];
                    Individual parent2 = pop[BiasedWheel(scores)];
                    Individual child = Crossover(parent1, parent2);
                    child.Mutate(algoGenParams.MutationRate);

                    nextGen.Add(child);
                }

                pop = nextGen;
            }
        }

        private void Elitism(List<float> scores, List<Individual> nextGen)
        {
            // from best to worst
            List<IndividualData> individualDatas = new List<IndividualData>();

            for (int j = 0; j < algoGenParams.PopulationSize; j++)
            {
                individualDatas.Add(new IndividualData(pop[j], scores[j]));
            }

            individualDatas.Sort((ind1, ind2) =>
            {
                if (ind1.fitness > ind2.fitness) return -1;
                if (ind1.fitness < ind2.fitness) return 1;
                return 0;
            });

            for (int j = 0; j < algoGenParams.BestKeptCount; j++)
            {
                nextGen.Add(individualDatas[j].individual);
            }
        }

        private Individual Crossover(Individual parent1, Individual parent2)
        {
            if(Random.Range(0f, 1f) < algoGenParams.CrossOverRate)
            {
                Individual child = new Individual(parametersData, numberOfBits);
                int cutPoint = Random.Range(1, numberOfBits - 1);
                child.CrossOver(parent1, parent2, cutPoint);
                return child;
            }

            return Random.Range(0, 2) == 0 ? parent1.Clone() : parent2.Clone();
        }

        private int BiasedWheel(List<float> normalizedScores)
        {
            float randomThreshold = 0;
            for (int i = 0; i < normalizedScores.Count; i++)
            {
                randomThreshold += normalizedScores[i];
                if(randomThreshold >= Random.Range(0f, 1f))
                {
                    return i;
                }
            }

            return normalizedScores.Count - 1;
        }

        private float MapValue(int val, float max)
        {
            return ExtensionMethods.Remap(val, 0, maxValBinary, 0, max);
        }
    }

    struct IndividualData
    {
        public Individual individual;
        public float fitness;

        public IndividualData(Individual individual, float fitness)
        {
            this.individual = individual;
            this.fitness = fitness;
        }
    }
}
