using System;

namespace Potucek_InsertionSort
{
    // Constants
    static class Constants
    {
        public const int LowerBound = 0;
        public const int UpperBound = 100;
        public const int ArraySize = 20;
    }

    static class Program
    {
        static int[] MakeArray(int size)
        {
            int[] arr = new int[size];
            Random random = new Random();

            for (int i = 0; i < arr.Length; i++)
            {
                arr[i] = random.Next(Constants.LowerBound, Constants.UpperBound);
            } 
            return arr;
        }

        static int[] InsertionSort(int[] arr)
        {
            for (int j = 1; j < arr.Length; ++j)
            {
                int stored = arr[j];
                int i = j - 1;

                while(i >= 0 && arr[i] > stored)
                {
                    arr[i+1] = arr[i];
                    i = i - 1;
                }
                arr[i+1] = stored;
            }
            return arr;
        }

        static int[] BubbleSort(int[] pole)
        {
            for (int i = 0; i < pole.Length; i++)
            {
                for (int j = 0; j < pole.Length - i - 1; j++)
                {
                    if (pole[j] > pole[j + 1])
                    {
                        int pom = pole[j];
                        pole[j] = pole[j + 1];
                        pole[j + 1] = pom;
                    }
                }
            }
            return pole;
        }
        static void PrintArray(int[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                Console.Write(arr[i] + ", ");
            }
            Console.WriteLine("");
        }

        static void Main()
        {
            int[] array = MakeArray(Constants.ArraySize);
            Console.WriteLine("Not sorted:");
            PrintArray(array);
            array = InsertionSort(array);
            Console.WriteLine("Sorted by Insertion sort: ");
            PrintArray(array);
            array = BubbleSort(array);
            Console.WriteLine("Sorted by Bubble sort: ");
            PrintArray(array);
        }
    }
}
