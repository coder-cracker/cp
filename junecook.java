import java.util.*;
import java.io.*;
class junecook
{
	public static void main(String []args)
	{
		FastScanner KB = new FastScanner();
		long T=KB.nextInt();
		for(long k=1;k<=T;k++)
		{
			long A=KB.nextLong();
			long B=KB.nextLong();
			long C=KB.nextLong();
			long D=KB.nextLong();
			long E=KB.nextLong();
					
			if(A+B<=D && C<=E)
			{
				System.out.println("YES");
			}
			else if(B+C<=D && A<=E)
			{
				System.out.println("YES");
			}
			else if(A+C<=D && B<=E)
			{
				System.out.println("YES");
			}
			else
			{
				System.out.println("NO");
			}
		}
	}
	
	static class FastScanner {
		public BufferedReader reader;
		public StringTokenizer tokenizer;
		public FastScanner() {
			reader = new BufferedReader(new InputStreamReader(System.in), 32768);
			tokenizer = null;
		}
		public String next() {
			while (tokenizer == null || !tokenizer.hasMoreTokens()) {
				try {
					tokenizer = new StringTokenizer(reader.readLine());
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
			return tokenizer.nextToken();
		}
		public int nextInt() {
			return Integer.parseInt(next());
		}
		public long nextLong() {
			return Long.parseLong(next());
		}
		public double nextDouble() {
			return Double.parseDouble(next());
		}
		public String nextLine() {
			try {
				return reader.readLine();
			} catch(IOException e) {
				throw new RuntimeException(e);
			}
		}
	}
}