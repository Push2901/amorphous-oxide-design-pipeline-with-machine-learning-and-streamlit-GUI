package model;

import layers.Layer;
import java.util.List;

public class InterfaceStack {
    private List<Layer> layers;

    public InterfaceStack(List<Layer> layers) {
        this.layers = layers;
    }

    public double effectiveStiffness() {
        double sum = 0.0;
        for (Layer l : layers) {
            sum += l.getModulus() * l.getThickness();
        }
        return sum;
    }
}

