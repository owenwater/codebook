/*
rectangle_cutting:
Cutting one rectangle by the others. Every cutting will make mostly
four new rectangles. The coordinates will be:
y[1] -------
|     |
|     |
y[0] -------
x[0]    x[1]
*/

struct rec
{
	/*rectangle*/
	void set(int x1, int x2, int y1, int y2)
	{
		/*build a vaild rectangle*/
		x[0] = min(x1,x2);
		x[1] = max(x1,x2);
		y[0] = min(y1,y2);
		y[1] = max(y1,y2);
	}	
	void set2(int x1, int x2, int y1, int y2)
	{
		/*build a rectangle, used by cutting rectangle, maybe invaild*/
		x[0] = x1;
		x[1] = x2;
		y[0] = y1;
		y[1] = y2;
	}
	bool same(rec other)
	{
		/*test if two rectangles are same*/
		return (this->x[0] == other.x[0]
			  &&this->x[1] == other.x[1]
			  &&this->y[0] == other.y[0]
			  &&this->y[1] == other.y[1]);

	}
	double calc()
	{
		/*calc the area of one rectangle*/
		return (x[1] - x[0]) * (y[1] - y[0]);
	}
	int x[2], y[2];
	bool check()
	{
		/*check the area is vaild or not*/
		return (this->x[0] < this->x[1] && this->y[0] < this->y[1]);
	}
	bool cover(rec cov)
	{
		/*check the other rectangle is cover this one or not*/
		return (this->x[0] >= cov.x[0] && this->x[1] <= cov.x[1]
		 && this->y[0] >= cov.y[0] && this->y[1] <= cov.y[1]);
	}
};

int cut(rec r, rec cut, rec res[])
{
	/*using rectangle "cut" cuts the rectangle "r".
	 *The result will be put into res[]
	  return the number of result.*/
	if (r.cover(cut))
		return 0;
	int n = 0;
	rec next[4];
	next[0].set2(r.x[0], min(cut.x[0], r.x[1]),
			     r.y[0], r.y[1]);
	next[1].set2(max(cut.x[1],r.x[0]), 
				 r.x[1], r.y[0], r.y[1]);
	next[2].set2(max(r.x[0], cut.x[0]), min(r.x[1], cut.x[1]), 
			      r.y[0], min(cut.y[0], r.y[1]));
	next[3].set2(max(r.x[0], cut.x[0]), min(r.x[1], cut.x[1]), 
			      max(cut.y[1], r.y[0]), r.y[1]);
	for (int i = 0; i < 4; i++)
	{
		if (!next[i].check())
			continue;
		for (int j = 0; j < i ; j++)
		{
			if (next[i].same(next[j]))
				break;
		}
		res[n] = next[i];
		n++;
	}
	return n;
}

/*
test:
just a test
*/

int main ()
{
	return 0;
}
