using System;

class  MyProgram
{
    static void Main()
    {
        string[] names = {"Wisdom", "Aniefiok", "Okposin"};
        Console.Write("My full name is: ");
        foreach (string name in names)
        {
            Console.Write($"{name}");
        }
    }
}