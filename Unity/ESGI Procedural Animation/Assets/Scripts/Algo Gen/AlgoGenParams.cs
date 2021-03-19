using UnityEngine;
using System.Collections;
using System.Collections.Generic;

namespace ESGI.AlgoGen
{
    [CreateAssetMenu(menuName = "ESGI/Algo Gen Params")]
    public class AlgoGenParams : ScriptableObject
    {
        [SerializeField, Min(0)] private int populationSize;
        [SerializeField, Min(0)] private int bestKeptCount;
        [SerializeField, Min(0)] private int numberOfGenerations;
        [SerializeField, Range(0, 1)] private float crossOverRate = 0.9f;
        [SerializeField, Range(0, 1)] private float mutationRate = 0.1f;

        public int PopulationSize { get => populationSize; }
        public int NumberOfGenerations { get => numberOfGenerations; }
        public float CrossOverRate { get => crossOverRate; }
        public float MutationRate { get => mutationRate; set => mutationRate = value; }
        public int BestKeptCount { get => bestKeptCount; set => bestKeptCount = value; }
    }
}
