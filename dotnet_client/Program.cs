using System;
using System.Collections.Generic;
namespace Game
{
    class Play {
        static int Count = 0;
        string Name;
        int ID;
        public Play(string Name)
        {
            this.ID = Count;
            Count++;
            this.Name = Name;
        }
    }
    class Client
    {
        List<Play> plays;
        public static void WriteLine(string line)
        {
            Console.WriteLine("<line>"+line+"</line>");
        }
        public Client() 
        {
            plays = new List<Play>();
            CreatePlays();
        }
        public void AddPlay(string play) {
            plays.Add(new Play(play));
        }
        public void CreatePlays(){
            AddPlay("attack");
            AddPlay("defend");
            AddPlay("dodge");
            AddPlay("think");
            AddPlay("breathe");
            AddPlay("counter");
            AddPlay("pray");
            AddPlay("eat");
        }
        public void Run()
        {
            WriteLine("Press any key to start playing...");
            Console.ReadKey(true);
            
            WriteLine("Choose a play...");
            WriteLine("Choose a play...");
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Client client = new Client();
            client.Run();
        }
    }
}
