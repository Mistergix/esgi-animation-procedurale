using UnityEngine;
using System.Collections;
using System.Diagnostics;
using System;
public class IB : MonoBehaviour
{

    // Use this for initialization
    void Start()
    {
        try
        {
            Process myProcess = new Process();
            myProcess.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            myProcess.StartInfo.CreateNoWindow = true;
            myProcess.StartInfo.UseShellExecute = false;
            myProcess.StartInfo.FileName = "C:/Users/Alain/Desktop/Anim & IA 4A/2 PROGRANIMALS FUNKBOXING/callBlenderScript.bat";
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


# Au final pour vendredi à 15H30, CC1
On est dans Unity , vous avez un bouton Import Creatures
Ce bouton lance ce process, qui appel le fichier BAT
Le BAT lance Blender en arrière-plan , qui crée des créatures
Les créatures sont loader en tant qu'Asset dans Unity
Demo dans Unity
Scripts dans Blender
Très modestement, ceci équivaut à faire une sorte de Blender Engine pour Unity
(comme Houdini Engine)