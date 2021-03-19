using UnityEngine;
using System.Collections;
using System.Collections.Generic;

namespace ESGI.AlgoGen
{
    [CreateAssetMenu(menuName = "ESGI/Algo Gen Individual Data")]
    public class ParametersData : ScriptableObject
    {
        [SerializeField, Min(0)] private int numberOfParameters = 6;
        [SerializeField, Min(0)] private float maxDistanceBetweenLegs;
        [SerializeField, Min(0)] private float maxKneeLengthX;
        [SerializeField, Min(0)] private float maxKneeLengthY;
        [SerializeField, Min(0)] private float maxFootLengthX;
        [SerializeField, Min(0)] private float maxFootLengthY;
        [SerializeField, Min(0)] private float maxDistanceHead;
        [SerializeField, Min(0)] private float maxNeckLengthX;
        [SerializeField, Min(0)] private float maxNeckLengthY;
        [SerializeField, Min(0)] private float maxHeadLengthX;
        [SerializeField, Min(0)] private float maxHeadLengthY;

        public float MaxDistanceBetweenLegs { get => maxDistanceBetweenLegs; }
        public float MaxDistanceHead { get => maxDistanceHead; }
        public int NumberOfParameters { get => numberOfParameters; }
        public float MaxNeckLengthX { get => maxNeckLengthX; set => maxNeckLengthX = value; }
        public float MaxNeckLengthY { get => maxNeckLengthY; set => maxNeckLengthY = value; }
        public float MaxHeadLengthX { get => maxHeadLengthX; set => maxHeadLengthX = value; }
        public float MaxHeadLengthY { get => maxHeadLengthY; set => maxHeadLengthY = value; }
        public float MaxKneeLengthX { get => maxKneeLengthX; set => maxKneeLengthX = value; }
        public float MaxKneeLengthY { get => maxKneeLengthY; set => maxKneeLengthY = value; }
        public float MaxFootLengthX { get => maxFootLengthX; set => maxFootLengthX = value; }
        public float MaxFootLengthY { get => maxFootLengthY; set => maxFootLengthY = value; }
    }
}
