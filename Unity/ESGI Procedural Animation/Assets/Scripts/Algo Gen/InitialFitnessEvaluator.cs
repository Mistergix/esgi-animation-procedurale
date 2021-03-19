using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using ESGI.AlgoGen;

namespace ESGI.AlgoGen
{
    public class InitialFitnessEvaluator : FitnessEvaluatorBase
    {
        public override float Fitness(Individual individual)
        {
            List<int> listtest=individual.InterpretedGenotype(8)
                float res = listtest[0]*0.3+listtest[1]*0.5+listtest[2]*0.5+listtest[3]*0.6 + listtest[4] * 0.6 + 0.9*(255-listtest[5]) + 0.8 * (255 - listtest[6]) + 0.8 * (255 - listtest[7]) + +0.9 * (255 - listtest[8]) + +0.9 * (255 - listtest[9])
            return res

        }
    }
}
