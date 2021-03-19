using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System;
using System.IO;
using UnityEditor;

namespace ESGI.BlenderPipelineESGI
{
    public class BlenderPipeline : MonoBehaviour
    {
        private void Start()
        {
            
        }
        public void CreateProcess(float distanceBetweenLegs, Vector2 kneeLength, Vector2 footLength, float distanceHead, Vector2 neckLength, Vector2 headLength, string creatureId)
        {
            string assetsDirPath = Application.dataPath;
            string projectDirPath = Directory.GetParent(assetsDirPath).FullName;
            string batsPath = Path.Combine(projectDirPath, "blender pipeline");

            string finalPath = Path.Combine(batsPath, "generateOneCreature.bat");

            string bat = File.ReadAllText(finalPath);

            string intoPath = Path.Combine(assetsDirPath, "EXPORTED CREATURES", $"{creatureId}.obj");

            string pythonPath = Path.Combine(assetsDirPath, "generateCreature.py");

            bat = bat
                .Replace("distanceBetweenLegs", distanceBetweenLegs.ToString())
                .Replace("kneeLengthX", kneeLength.x.ToString())
                .Replace("kneeLengthY", kneeLength.y.ToString())
                .Replace("footLengthX", footLength.x.ToString())
                .Replace("footLenghtY", footLength.y.ToString())
                .Replace("distanceHead", distanceHead.ToString())
                .Replace("neckLengthX", neckLength.x.ToString())
                .Replace("neckLengthY", neckLength.y.ToString())
                .Replace("headLengthX", headLength.x.ToString())
                .Replace("headLengthY", headLength.y.ToString())
                .Replace("pythonPath", $"\"{pythonPath}\"")
                .Replace("oPath", $"\"{intoPath}\"");

            File.WriteAllText(Path.Combine(assetsDirPath, "generateOneCreature.bat"), bat);
            


            try
            {
                Process myProcess = new Process();
                myProcess.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
                myProcess.StartInfo.CreateNoWindow = true;
                myProcess.StartInfo.UseShellExecute = false;
                myProcess.StartInfo.FileName = Path.Combine(assetsDirPath, "generateOneCreature.bat");
                myProcess.EnableRaisingEvents = true;
                myProcess.Start();
                myProcess.WaitForExit();
                int ExitCode = myProcess.ExitCode;
                print(ExitCode);
            }
            catch (Exception e)
            {
                print(e);
            }

            AssetDatabase.Refresh();
        }
    }
}
