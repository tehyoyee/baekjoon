
width = 51
height = 37
diagonals = [[17, 19]]
# width = 2
# height = 2
# diagonals = [[1, 1], [2, 2]]



# def fact(x):
# 	if x > 1:
# 		return x * fact(x-1)
# 	return 1

# def solution(width, height, diagonals):
# 	result = 0
# 	for cx, cy in diagonals:
# 		tmp = 1
# 		tmp *= (fact(cx-1 + cy) // (fact(cx-1) * fact(cy)))
# 		tmp *= (fact(width - cx + height - (cy - 1)) // (fact(width - cx) * fact(height - (cy - 1))))
# 		result += tmp
# 		result %= 10000019
# 		tmp = 1
# 		tmp *= (fact(cx + cy-1) // (fact(cx) * fact(cy-1)))
# 		tmp *= (fact(width - (cx - 1) + height - (cy)) // (fact(width - (cx - 1)) * fact(height - cy)))
# 		result += tmp
# 		result %= 10000019
# 	return result

# print(solution(width, height, diagonals))





import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        int width = 51;
        int height = 37;
        int[][] diagonals = {{17, 19}};
        // int width = 2;
        // int height = 2;
        // int[][] diagonals = {{1, 1}, {2, 2}};
        System.out.println(solution(width, height, diagonals));
    }
    
    public static BigInteger fact(int x) {
        if (x > 1) {
            return BigInteger.valueOf(x).multiply(fact(x-1));
        }
        return BigInteger.ONE;
    }

    public static BigInteger solution(int width, int height, int[][] diagonals) {
        BigInteger result = BigInteger.ZERO;
        for (int[] coords : diagonals) {
            int cx = coords[0];
            int cy = coords[1];
            BigInteger tmp = BigInteger.ONE;
            tmp = tmp.multiply(fact(cx-1 + cy).divide(fact(cx-1).multiply(fact(cy))));
            tmp = tmp.multiply(fact(width - cx + height - (cy - 1)).divide(fact(width - cx).multiply(fact(height - (cy - 1)))));
            result = result.add(tmp);
            result = result.mod(BigInteger.valueOf(10000019));
            tmp = BigInteger.ONE;
            tmp = tmp.multiply(fact(cx + cy - 1).divide(fact(cx).multiply(fact(cy-1))));
            tmp = tmp.multiply(fact(width - (cx - 1) + height - (cy)).divide(fact(width - (cx - 1)).multiply(fact(height - cy))));
            result = result.add(tmp);
            result = result.mod(BigInteger.valueOf(10000019));
        }
        return result;
    }
}
