package org.opentutorials.numberstring;

public class CharString {

	public static void main(String[] args) {
		// 문자는 작은따옴표로 감싼다.
		System.out.println('생');
		// 문자열은 큰따옴표르 감싸야함
		System.out.println("생활코딩");
//		 문자열을 작은 따옴표로 감싸면 에러발생
//		System.out.println('생활코딩');
//		한 글자도 문자열이 될 수 있기 때문에 큰따옴표로 감싼다고 에러가 발생하진 않는다.
		System.out.println("생");
//		문자열의 연산
		System.out.println("생활코딩" + "입니다");
//		문자열 이므로 11
		System.out.println("1"+"1");
//		작은따옴표로 하면 문자로 인식 아스키코드에 따라 처리되는듯 98나옴
		System.out.println('1'+'1');
		
//		큰따옴표를 넣기위한 방법 \이용! 이스케이프!
		System.out.println("egoing said \"Welcome programming world\"");
//		여려줄의 표시 \n 줄바꿈 이용! 
		System.out.println("HTML\nCSS\nJavaScript\n");
	}

}
