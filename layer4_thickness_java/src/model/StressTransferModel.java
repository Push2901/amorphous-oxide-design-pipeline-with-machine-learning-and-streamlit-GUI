package model;

public class StressTransferModel {

    public static double failureRisk(double stiffness, double oxideThickness) {
        double embrittlementPenalty = Math.max(0, oxideThickness - 10.0);
        return stiffness * 1e-4 + embrittlementPenalty * 0.2;
    }
}
