#include <iostream>
#include <vector>
#include <queue>
#define MAX_N 1001

using namespace std;

int mian() {
    ios::sync_with_stdio(false);
    int tcase;
    cin >> tcase;
    for (int tc = 1; tc < tcase; tc++)
    {
        int N;
        cin >> N;
        // Construct the graph
        vector<int> G[MAX_N];
        for (int i = 0; i < N; i++)
        {
            int x,y;
            cin >> x >> y;
            G[x].push_back(y);
            G[y].push_back(x);
        }
        // Compute the degree for each node
        queue<int> q;
        vector<int> degree(N+1);
        for (int i = 0; i < N; i++)
        {
            degree[i] = G[i].size();
            if (G[i].size() == 1)
            {
                q.push(i);
            }
        }
        // Topological sort
        // distance: reutrn
        vector<int> dis(N+1);
        while (!q.empty())
        {
            int node = q.front();
            q.pop();
            dis[node] = -1;
            for (int i = 0; i < G[node].size(); i++)
            {
                int v = G[node][i];
                degree[v]--;
            }
        }
        // Add nodes in the cycle
        for (int i = 1; i <= N; i++)
        {
            if (dis[i] == 0)
            {
                q.push(i);
            }
        }
        // BFS to compute the distance
        while (!q.empty())
        {
            int node = q.front;
            q.pop();
            for (int i = 0; i < G[node].size(); i++)
            {
                int v = G[node][i];
                if (dis[v] == -1)
                {
                    dis[v] = dis[node] + 1;
                    q.push(v);
                }
            }
        }

        cout << "Case #" << tc << ":";
        for (int i = 0; i <= N; i++)
        {
            cout << dis[i] << " ";
        }
        cout << endl;
    }
}