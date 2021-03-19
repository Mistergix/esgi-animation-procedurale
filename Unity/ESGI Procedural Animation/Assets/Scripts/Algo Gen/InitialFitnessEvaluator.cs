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
            return Random.Range(0, 11f);
        }
    }
}
