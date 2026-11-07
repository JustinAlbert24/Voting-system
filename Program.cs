Console.WriteLine("Input number : ");
string number = Console.ReadLine();
int numberFlow = Convert.ToInt32(number);
if (numberFlow % 2 == 0)
    Console.WriteLine("Tick");
else
    Console.WriteLine("Tock");