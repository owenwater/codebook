#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <ctime>
#include <string>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cctype>
#include <stack>

#define inputfilename "input"
#define outputfilename "a.out"

using namespace std;

/*codebook start*/
stack <string> ops;
stack <int> value;

int token(string s, int &p, string &op)
{
	int v = 0;
	if (s[p] >= '0' && s[p] <= '9')
	{
		while (p < s.length() && s[p] >= '0' && s[p] <= '9')
		{
			v = v * 10 + (s[p++] - '0');
		}
		return v;
	}
	else
	{
		op = s[p++];
		return -1;
	}

}

int priority(string op)
{
	if (op == "+" || op == "-")
		return 1;
	if (op == "*" || op == "/")
		return 2;
	if (op == "(")
		return -1;
	if (op == "@")
		return -1;
	return 0;
}

int pop_and_calc()
{
	string op =ops.top();
	ops.pop();
	if (op == "@")
	{
		if (value.size() != 1)
		{
			throw("exp error");
		}
		return 0;
	}
	int v[2];
	for (int i = 0 ; i <2; i++)
	{
		if (value.empty())
		{
			throw("exp error");
		}
		v[i] = value.top();
		value.pop();
	}
	if (op == "+")
	{
		value.push(v[0] + v[1]);
	}
	else if (op == "-")
	{
		value.push(v[1] - v[0]);
	}
	else if (op == "*")
	{
		value.push(v[0] * v[1]);
	}
	else if (op == "/")
	{
		if (v[0] == 0)
		{
			throw ("div zero");
		}
		value.push(v[1] / v[0]);
	}
	else if (op == "@")
	{
	}
	return 0;
}

int calc(string s)
{
	while (!ops.empty()) ops.pop();
	while (!value.empty()) value.pop();
	ops.push("@");
	int p = 0;
	while (p < s.length())
	{
		string op;
		int rt = token(s, p, op);
		if (rt != -1)
		{
			value.push(rt);
		}
		else
		{
			if (op == "(")
				ops.push(op);
			else if (op == ")")
			{
				while (true)
				{	
					if (ops.empty())
					{
						throw("exp error");
					}
					if (ops.top() == "(")
					{
						ops.pop();
						break;
					}
					pop_and_calc();
				}
			}
			else
			{
				while (true)
				{
					if (ops.empty())
					{
						throw ("exp error");
					}
					if (priority(ops.top()) < priority(op))
					{
						break;
					}
					pop_and_calc();
				}
				ops.push(op);
			}
		}
	}
	while (!ops.empty())
	{
		pop_and_calc();
	}
	int v = value.top();
	value.pop();
	return v;
	
}

/*codebook end*/


int main ()
{
	freopen(inputfilename , "r" , stdin);
	/*freopen(outputfilename , "w" , stdout);*/
	
	string s;
	while (cin >> s)
	{
		try
		{
			cout << calc(s) << endl;
		}
		catch (const char *s)
		{
			string msg(s);
			cout << msg << endl;
		}
	}



	return 0;
}

 
