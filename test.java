import java.util.*;

public class test {

    public static void main(String[] args) {
        Member member1 = new Member("다", 10);
        Member member2 = new Member("나", 10);
        Member member3 = new Member("가", 12);
        Member member4 = new Member("가", 9);

        List<Member> members = new ArrayList<>();
        members.add(member1);
        members.add(member2);
        members.add(member3);
        members.add(member4);
        
        // 정렬 전 members: {"다", 10}, {"나", 10}, {"가", 12}, {"가", 9}
        
        // 정렬
        members = members.sort(comparing(Member::getName)
            .thenComparing(Member::getAge));

        // 정렬 후 members: {"가", 9}, {"가", 12}, {"나", 10}, {"다", 10}
    }

	static public class Member {

    private String name;
    private int age;

    public Member(String name, int age){
    	this.name = name;
    	this.age = age;
    }

    public String getName() {
    	return name;
    }

    public int getAge() {
    	return age;
    }
}

// Member
