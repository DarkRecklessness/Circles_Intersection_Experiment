#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ull = unsigned long long;
using ld = long double;
using ql = __int128_t;

const int N = 3;
mt19937 rng(69426942);

double rnd(double min, double max) {
    double zero_one = (double)rng() / UINT32_MAX;
    return min + zero_one * (max - min);
}

bool check(double x_c, double y_c, double r, double x, double y) {
    double dx = x - x_c;
    double dy = y - y_c;
    return dx * dx + dy * dy <= r * r;
}

double get_ans(vector<array<double, 3>>& cir,
               double min_x, double max_x, double min_y, double max_y,
               double cnt_generated) {
    int cnt_in_intersect = 0;
    for (int i = 0; i < cnt_generated; ++i) {
        double x = rnd(min_x, max_x);
        double y = rnd(min_y, max_y);
        bool in = true;
        for (auto& c : cir) {
            in &= check(c[0], c[1], c[2], x, y);
        }
        cnt_in_intersect += in;
    }
    double s = (max_y - min_y) * (max_x - min_x);
    return ((double)cnt_in_intersect / cnt_generated) * s;
}

double wide(vector<array<double, 3>>& cir, int cnt_generated) {
    double min_x = cir[0][0] - cir[0][2];
    double min_y = cir[0][1] - cir[0][2];
    double max_x = cir[0][0] + cir[0][2];
    double max_y = cir[0][1] + cir[0][2];
    for (int i = 1; i < N; ++i) {
        min_x = min(min_x, cir[i][0] - cir[i][2]);
        min_y = min(min_y, cir[i][1] - cir[i][2]);
        max_x = max(max_x, cir[i][0] + cir[i][2]);
        max_y = max(max_y, cir[i][1] + cir[i][2]);
    }

    return get_ans(cir, min_x, max_x, min_y, max_y, cnt_generated);
}

double narrow(vector<array<double, 3>>& cir, int cnt_generated) {
    double min_x = cir[0][0] - cir[0][2];
    double min_y = cir[0][1] - cir[0][2];
    double max_x = cir[0][0] + cir[0][2];
    double max_y = cir[0][1] + cir[0][2];
    // find the minimum area for the intersection
    for (int i = 1; i < N; ++i) {
        min_x = max(min_x, cir[i][0] - cir[i][2]);
        min_y = max(min_y, cir[i][1] - cir[i][2]);
        max_x = min(max_x, cir[i][0] + cir[i][2]);
        max_y = min(max_y, cir[i][1] + cir[i][2]);
    }

    return get_ans(cir, min_x, max_x, min_y, max_y, cnt_generated);
}

// cir - dataa of circles
// mode = false, wide area
// mode = true, narrow area
double calculate(vector<array<double, 3>>& cir, int cnt_generated, bool mode) {
    if (mode) return narrow(cir, cnt_generated);
    return wide(cir, cnt_generated);
}

// void solve() {
//     vector<array<double, 3>> cir(N);
//     for (int i = 0; i < N; ++i) {
//         for (int j = 0; j < 3; ++j) {
//             cin >> cir[i][j];
//         }
//     }
//     // false -> wide area
//     double ans = calculate(cir, 5e5, false);
//     cout << ans << '\n';
// }

void solve() {
    vector<array<double, 3>> cir(N);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < 3; ++j) {
            cin >> cir[i][j];
        }
    }

    cout << "N,Area_Wide,Area_Narrow\n";
    for (int cnt_generated = 100; cnt_generated <= 100'000; cnt_generated += 500) {
        cout << cnt_generated << ',';
        cout << calculate(cir, cnt_generated, false) << ',';
        cout << calculate(cir, cnt_generated, true) << '\n';
    }
}

signed main() {
#ifdef DarkReck
    freopen("..\\input.txt", "r", stdin);
    freopen("..\\output.txt", "w", stdout);
#endif
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    cout << fixed << setprecision(10);

    solve();
}