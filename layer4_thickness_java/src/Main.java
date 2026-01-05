
import layers.*;
import model.*;

import java.io.FileWriter;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws Exception {

        FileWriter writer = new FileWriter("outputs/thickness_results.csv");

        writer.write("oxide_thickness,stiffness,failure_risk\n");

        for (double t = 0.0; t <= 30.0; t += 1.0) {

            OxideLayer oxide = new OxideLayer(t);
            PolymerLayer polymer = new PolymerLayer();
            MetalLayer metal = new MetalLayer();

            InterfaceStack stack = new InterfaceStack(
                    Arrays.asList(metal, oxide, polymer)
            );

            double stiffness = stack.effectiveStiffness();
            double risk = StressTransferModel.failureRisk(stiffness, t);

            writer.write(t + "," + stiffness + "," + risk + "\n");
        }

        writer.close();
        System.out.println("Layer 4 complete. Thickness sweep done.");
    }
}
