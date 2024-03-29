using System;
using System.Collections.Generic;

public class Graph
{
    private int vertices;
    private List<int>[] adj;

    public Graph(int v)
    {
        vertices = v;
        adj = new List<int>[v];

        for (int i = 0; i < v; i++)
        {
            adj[i] = new List<int>();
        }
    }

    public void AddEdge(int v, int w)
    {
        adj[v].Add(w);
    }

    public void BFS(int start)
    {
        bool[] visited = new bool[vertices];

        Queue<int> queue = new Queue<int>();
        visited[start] = true;
        queue.Enqueue(start);

        while (queue.Count != 0)
        {
            start = queue.Dequeue();
            Console.Write(start + " ");

            foreach (int i in adj[start])
            {
                if (!visited[i])
                {
                    visited[i] = true;
                    queue.Enqueue(i);
                }
            }
        }
    }
}

public class Program
{
    public static void Main()
    {
        Graph g = new Graph(4);
        g.AddEdge(0, 1);
        g.AddEdge(0, 2);
        g.AddEdge(1, 2);
        g.AddEdge(2, 0);
        g.AddEdge(2, 3);
        g.AddEdge(3, 3);

        Console.WriteLine("BFS starting from vertex 2:");
        g.BFS(2);
    }
}
