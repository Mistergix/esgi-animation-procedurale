using UnityEngine;
using System.Collections;
using System.Collections.Generic;

namespace ESGI.AlgoGen
{
    public abstract class FitnessEvaluatorBase : ScriptableObject
    {
        public abstract float Fitness(Individual individual);
    }
}
