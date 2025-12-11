import java.util.*;

public class leadership_styles_questionnaire {

    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {

        Scanner scanner= new Scanner(System.in);

        int[] scores= new int[12];
        String[] questions= {"I give clear explanations of what is expected of others.",
            "I show interest in followers’ personal concerns.",
            "I invite followers to participate in decision making.",
            "I challenge followers to continuously improve their work performance.",
            "I give followers explicit instructions for how to do their work.",
            "I show concern for the personal well-being of my followers.",
            "I solicit followers’ suggestions before making a decision.",
            "I encourage followers to consistently raise their own standards of performance.",
            "I give clear directions to others for how to proceed on a project.",
            "I listen to others and give them encouragement.",
            "I am receptive to ideas and advice from others.",
            "I expect followers to excel in all aspects of their work."
        };
        String definitions= "Respond with the frequency you do this behavior by typing the following: " +
        "'1' for never, '2' for seldom, '3' for sometimes, '4' for often, and '5' for always";

        for (int i = 0; i < scores.length; i++) {
            System.out.println(definitions);
            System.out.println(questions[i]);
            scores[i]= scanner.nextInt();
            System.out.println();
            System.out.println();
        }

        scanner.close();

        int[] finalScores= new int[4];

        finalScores[0]= scores[0] + scores[4] + scores[8];
        finalScores[1]= scores[1] + scores[5] + scores[9];
        finalScores[2]= scores[2] + scores[6] + scores[10];
        finalScores[3]= scores[3] + scores[7] + scores[11];

        int largest= finalScores[0];

        for (int i = 1; i < finalScores.length; i++) {
            if (largest < finalScores[i]) {
                largest= finalScores[i];
            }
        }

        if (largest == finalScores[0]) {
            System.out.println("Your leadership style is: Directive Leadership");
        } else if (largest == finalScores[1]) {
            System.out.println("Your leadership style is: Supportive Leadership");
        } else if (largest == finalScores[2]) {
            System.out.println("Your leadership style is: Participative Leadership");
        } else {
            System.out.println("Your leadership style is: Achievement-oriented Leadership");
        }

    }
}