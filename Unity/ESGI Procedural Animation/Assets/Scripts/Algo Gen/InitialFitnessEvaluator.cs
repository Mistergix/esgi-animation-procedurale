using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using ESGI.AlgoGen;

namespace ESGI.AlgoGen
{
    [CreateAssetMenu(menuName = "ESGI/Fitness Evaluator/Initial")]
    public class InitialFitnessEvaluator : FitnessEvaluatorBase
    {
        
        public override float Fitness(Individual individual)
        {
            List<int> listtest = individual.InterpretedGenotype(8);
            float res = listtest[0] * 0.3f + listtest[1] * 0.5f + listtest[2] * 0.5f + listtest[3] * 0.6f + listtest[4] * 0.6f + 0.9f * (255 - listtest[5]) + 0.8f * (255 - listtest[6]) + 0.8f * (255 - listtest[7]) + 0.9f * (255 - listtest[8]) + 0.9f * (255 - listtest[9]);
            return res;
        }
    }
}
