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
        public double maxHealth = 64;
        public double health = 64;
        public double energy = 32;
        public double strength = 4;
        public double intelligence = 8;
        public double armor = 16;
        public double resistance = 8;
        public double discipline = 4;
        public double courage = 4;

        public bool TakeDamage(double damage)
        {
            if (damage >= health)
            {
                health = 0;
                return true;
            }
            health -= damage;
            return false;
        }

        public void Tick()
        {

            if (health + 1 > maxHealth)
            {
                health = maxHealth;
            }
            else
            {
                health += 1;
            }
        }
    }
    public enum PlayType
    {
        Attack,
        Defend,
        Think,
        Breathe,
        Pray,
        Eat,
        Forge,
    }
    class Client
    {
        Player PlayerA;
        Player PlayerB;
        List<Play> Plays;
        Player[] players;
        Play[] choosenPlays;
        int Turn = 0;
        public static void WriteLine(string line)
        {
            Console.WriteLine("<Line> "+line+" </Line>");
        }
        public Client() 
        {
            PlayerA = new Player();
            PlayerB = new Player();
            players = new Player[2];
            choosenPlays = new Play[2];
            Plays = new List<Play>();
            CreatePlays();
        }
        public void AddPlay(string play) {
            Plays.Add(new Play(play));
        }
        public void CreatePlays(){
            AddPlay("Attack");
            AddPlay("Defend");
            AddPlay("Think");
            AddPlay("Breathe");
            AddPlay("Pray");
            AddPlay("Eat");
            AddPlay("Forge");
        }
        public Play ChoosePlay(bool turnType) {
            WriteLine("Choose a play...");
            foreach (Play play in Plays)
            {
                WriteLine("Index: " + play.Index + " ,Play: " + play.Name);
            }
            Console.Write("<Input> ");
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
                    return ChoosePlay(turnType);
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
                return ChoosePlay(turnType);
            }
        }
        public bool ApplyRules(Player player1, Player player2)
        {
            if (choosenPlays[0].Index == (int)PlayType.Attack)
            {
                double balance;
                if (player1.energy > 0)
                {
                    balance = player1.strength*(player1.courage/player2.courage)-player2.resistance - player2.armor*2;
                }
                else
                {
                    balance = (player1.courage/player2.courage)-player2.resistance - player2.armor*2;

                }
                if (balance >= 0)
                {
                    if (player2.TakeDamage(balance-player2.intelligence)) 
                    {
                        return false;
                    }
                }
                else
                {
                    if (player1.TakeDamage(0-balance+player2.intelligence)) 
                    {
                        return false;
                    }
                }
                player1.energy--;
            } 
            else if (choosenPlays[0].Index == (int)PlayType.Breathe)
            {   
                player1.strength+=1.0/2.0;
                player1.energy++;
            }
            else if (choosenPlays[0].Index == (int)PlayType.Defend)
            {
                player1.health++;
                player1.resistance++;
            }
            else if (choosenPlays[0].Index == (int)PlayType.Eat)
            {
                player1.health++;
                player1.maxHealth++;
            }
            else if (choosenPlays[0].Index == (int)PlayType.Pray)
            {
                player1.strength+=1.0/2.0;
                player1.courage++;
            }
            else if (choosenPlays[0].Index == (int)PlayType.Think)
            {
                player1.intelligence++;
            }
            else if (choosenPlays[0].Index == (int)PlayType.Forge)
            {
                player1.strength++;
                player1.armor++;
            }
            return true;
            
        }
        public void PrintPlayerAttributes(Player player)
        {
            WriteLine("Health: " + player.health);
            WriteLine("MaxHealth: " + player.maxHealth);
            WriteLine("Strength: " + player.strength);
            WriteLine("Armor: " + player.armor);
            WriteLine("Resistance: " + player.resistance);
            WriteLine("Intelligence: " + player.intelligence);
            WriteLine("Energy: " + player.energy);
            WriteLine("Courage: " + player.courage);
        }
        public void PrintPlayersAttributes()
        {
            Console.WriteLine();
            WriteLine("Player A attributes:");
            PrintPlayerAttributes(PlayerA);
            Console.WriteLine();
            WriteLine("Player B attributes:");
            PrintPlayerAttributes(PlayerB);
        }
        public bool PlayTurn(bool turnType)
        {
            bool status;   
            if (turnType)
            {
                players[0] = PlayerA;
                players[1] = PlayerB;
            }
            else
            {
                players[1] = PlayerA;
                players[0] = PlayerB;
            }
            players[0].Tick();
            players[1].Tick();
            WriteLine("Turn: " + Turn);
            Console.WriteLine();
            if (turnType)
            {
                WriteLine("Player: A");
            }
            else
            {
                WriteLine("Player: B");
            }
            choosenPlays[0] = ChoosePlay(false);
            status = ApplyRules(players[0], players[1]);
            PrintPlayersAttributes();
            Console.WriteLine();
            if (status == false)
            {
                return false;
            }
            if (turnType)
            {
                WriteLine("Player: B");

            }
            else
            {
                WriteLine("Player: A");
            }
            choosenPlays[1] = ChoosePlay(true);
            
            status = ApplyRules(players[1], players[0]);
            PrintPlayersAttributes();
            return status;
        }
        public void Run()
        {
            WriteLine("Press any key to start playing...");
            Console.Write("<Input> ");
            Console.ReadKey(true);
            Console.WriteLine();
            bool playing = true;
            bool turn = true;
            while (playing)
            {
                playing = PlayTurn(turn);
            }
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
