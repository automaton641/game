using System;
using System.Collections.Generic;
namespace Game
{
    class Play {
        public static int Count = 0;
        public string Name;
        public int Index;
        public Play(string Name)
        {
            this.Index = Count;
            Count++;
            this.Name = Name;
        }
    }
    class Player 
    {
        int health;
        int energy;
        int strength;
        int intelligence;
        int armor;
        int resistance;
        int discipline;
        int courage;
    }
    class Client
    {
        Player player;
        List<Play> Plays;
        public static void WriteLine(string line)
        {
            Console.WriteLine("<Line>"+line+"</Line>");
        }
        public Client() 
        {
            Plays = new List<Play>();
            CreatePlays();
        }
        public void AddPlay(string play) {
            Plays.Add(new Play(play));
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
        public Play ChoosePlay() {
            WriteLine("Choose a play...");
            foreach (Play play in Plays)
            {
                WriteLine("Index: " + play.Index + " ,Play: " + play.Name);
            }
            string input = Console.ReadLine();
            int choosenIndex = 0;
            bool isNumeric = int.TryParse(input, out choosenIndex);
            if (isNumeric)
            {
                if (choosenIndex >= 0 && choosenIndex < Plays.Count)
                {
                    return Plays[choosenIndex];
                }
                else
                {
                    WriteLine("Not a valid play index, try again...");
                    return ChoosePlay();
                }
            }
            else
            {
                choosenIndex = 0;
                foreach (Play play in Plays)
                {
                    if (string.Equals(input, play.Name, StringComparison.OrdinalIgnoreCase))
                    {
                        return Plays[choosenIndex];
                    }
                    choosenIndex++;
                }
                WriteLine("Not a valid play name, try again...");
                return ChoosePlay();
            }
        }
        public void Run()
        {
            WriteLine("Press any key to start playing...");
            Console.ReadKey(true);
            Play play = ChoosePlay();
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
