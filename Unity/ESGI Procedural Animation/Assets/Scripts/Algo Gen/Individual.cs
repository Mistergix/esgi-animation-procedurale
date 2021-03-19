using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System;

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
            genotype = Enumerable.Repeat(false, nbBits).Select(bit => UnityEngine.Random.Range(0, 2) == 0).ToList();
        }

        public List<int> InterpretedGenotype(int nbBitsPerParam)
        {
            List<int> values = new List<int>();

            int begin = 0;

            for (int i = 0; i < nbBits / nbBitsPerParam; i++)
            {
                List<bool> bools = genotype.Skip(begin).Take(nbBitsPerParam).ToList();
                values.Add(Interpret(bools));
                begin += nbBitsPerParam;
            }

            return values;
        }

        private int Interpret(List<bool> bools)
        {
            string res = ToString(bools);
            return Convert.ToInt32(res, 2);
        }

        private string ToString(List<bool> bools)
        {
            StringBuilder sb = new StringBuilder();

            foreach (bool bit in bools)
            {
                sb.Append(bit ? "1" : "0");
            }

            return sb.ToString();
        }

        public override string ToString()
        {
            return ToString(genotype);
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
                if(UnityEngine.Random.Range(0f, 1f) < mutationRate)
                {
                    genotype[i] = !genotype[i];
                }
            }
        }
    }
}
