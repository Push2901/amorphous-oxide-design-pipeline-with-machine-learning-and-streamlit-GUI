package layers;

public abstract class Layer {
    protected double thickness;   // nm
    protected double modulus;     // GPa

    public Layer(double thickness, double modulus) {
        this.thickness = thickness;
        this.modulus = modulus;
    }

    public double getThickness() {
        return thickness;
    }

    public double getModulus() {
        return modulus;
    }
}
