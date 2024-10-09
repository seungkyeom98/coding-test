import java.util.Arrays;
class Solution {
    public int solution(int[] array) {
        int answer = 0;
       // int[] ar= new int[array.length];
        int temp=0; //임시저장 용도.
        
        //버블sort정렬방법
		// for(int k=1; k<array.length;k++) {
		// 	for(int i=0; i<array.length-k; i++) {
		// 		if(array[i]>array[i+1]) {
		// 				temp= array[i];//temp:temporary=일시적인->임시 변수이름(=임시 저장공간 이름)
		// 				array[i]=array[i+1]; //rep: repeat=반복한다 -> 반복 변수이름(= 반복 저장공간 이름)
		// 				array[i+1]=temp;
		// 		}
		// 	}
		// }
        Arrays.sort(array); // 내장 정렬 사용
        answer=array[array.length/2];
        return answer;
    }
    
    
    
}




