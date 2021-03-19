using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ESGI.AlgoGen
{
    public class Individual
    {
        private ParametersData data;
        private List<bool> genotype;
        private int nbBits;

        public Individual(ParametersData data, int numberOfBits)
        {
            this.data = data;
            nbBits = numberOfBits;
            RandomIndividual();
        }

        private void RandomIndividual()
        {
            genotype = Enumerable.Repeat(false, nbBits).Select(bit => Random.Range(0, 2) == 0).ToList();
        }

        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();

            foreach (bool bit in genotype)
            {
                sb.Append(bit ? "1" : "0");
            }

            return sb.ToString();
        }

        internal Individual Clone()
        {
            Individual c = new Individual(data, nbBits);
            c.genotype = new List<bool>(genotype);
            return c;
        }

        internal void CrossOver(Individual parent1, Individual parent2, int cutPoint)
        {
            genotype = parent1.genotype.Take(cutPoint).Concat( parent2.genotype.Skip(cutPoint)).ToList();
        }

        internal void Mutate(float mutationRate)
        {
            for (int i = 0; i < nbBits; i++)
            {
                if(Random.Range(0f, 1f) < mutationRate)
                {
                    genotype[i] = !genotype[i];
                }
            }
        }
    }
}
