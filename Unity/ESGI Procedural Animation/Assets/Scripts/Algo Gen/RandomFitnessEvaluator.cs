using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using ESGI.AlgoGen;

namespace ESGI.AlgoGen
{
    [CreateAssetMenu(menuName = "ESGI/Fitness Evaluator/Random")]
    public class RandomFitnessEvaluator : FitnessEvaluatorBase
    {
        [SerializeField, Min(0)] private float max = 10;
        public override float Fitness(Individual individual)
        {
            return Random.Range(0, max);
        }
    }
}
