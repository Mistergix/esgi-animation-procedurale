using UnityEngine;
using System.Collections;
using System.Collections.Generic;

namespace ESGI.Utilities
{
    public static class ExtensionMethods
    {
        public static float Remap(float val, float from1, float to1, float from2, float to2)
        {
            return (val - from1) / (to1 - from1) * (to2 - from2) + from2;
        }

    }
}
