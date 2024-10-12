class Solution {
    public int[] solution(int n) {
        // 홀수 개수를 미리 계산
        int[] answer = new int[(n + 1) / 2];
        
        int index = 0; // 배열에 값을 넣기 위한 별도의 인덱스
        
        // 1부터 n까지 반복하면서 홀수만 배열에 저장
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 1) {
                answer[index] = i;
                index++; // 값이 추가될 때마다 배열 인덱스를 증가
            }
        }
        
        return answer;
    }
}