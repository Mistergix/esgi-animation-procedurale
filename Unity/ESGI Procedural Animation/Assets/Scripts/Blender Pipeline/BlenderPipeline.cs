using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System;
using System.IO;

namespace ESGI.BlenderPipeline
{
    public class BlenderPipeline : MonoBehaviour
    {
        private void Start()
        {
        }
        private void CreateProcess(float distanceBetweenLegs, Vector2 kneeLength, Vector2 footLength, float distanceHead, Vector2 neckLength, Vector2 headLength)
        {
            string assetsDirPath = Application.dataPath;
            string projectDirPath = Directory.GetParent(assetsDirPath).FullName;
            string batsPath = Path.Combine(projectDirPath, "blender pipeline");

            string finalPath = Path.Combine(batsPath, "generateOneCreature.bat");

            string bat = File.ReadAllText(finalPath);

            bat = bat.Replace("", "");

            try
            {
                Process myProcess = new Process();
                myProcess.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
                myProcess.StartInfo.CreateNoWindow = true;
                myProcess.StartInfo.UseShellExecute = false;
                myProcess.StartInfo.FileName = finalPath;
                myProcess.EnableRaisingEvents = true;
                myProcess.Start();
                myProcess.WaitForExit();
                int ExitCode = myProcess.ExitCode;
                print(ExitCode);
                print("ok");
            }
            catch (Exception e)
            {
                print(e);
            }
        }
    }
}
