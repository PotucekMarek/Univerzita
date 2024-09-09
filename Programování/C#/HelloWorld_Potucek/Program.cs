using System;

namespace HelloWorld_Potucek
{
    class Program
    {
        static void Main()
        {
            HelloWorld();
        }
        static void HelloWorld()
        {
            Console.WriteLine("Hello World!");
            HelloWorld();
        }
    }
}
