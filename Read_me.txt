1. PSC_HTL_free_opt_model.def contains the SCAPS parameters used for the optimized case. These parameters can be modified as needed.

2. HTL_free_batch_setup.sbf contains the SCAPS batch setup parameters (features) used to generate the dataset, excluding degradation. Degradation values can be obtained by varying the defect density over time.

3. HTL_free_recorder_setup.srf includes the SCAPS recorder setup parameters (targets) used to record the corresponding performance metrics.

4. Trained_4_degree_Polynomial_Regressor.pkl contains the trained 4th-degree polynomial regressor model. It predicts normalized target values (η and Δ) from normalized features. The predicted targets can be denormalized using min-max scaling. For power conversion efficiency (η), the min and max values are 10.221 and 16.701, and for degradation (Δ), they are 0.034 and 1.552.

5. Trained_MLP_Classifier.h5 contains the trained multilayer perceptron (MLP) classifier, which can be used to determine whether given fabrication parameters lead to superior performance.

6. PSC_HTL_free_Dataset_IIM.xlsx contains the dataset of 1650 samples, with the following features: EG (eV), EA (eV), x (%), NABS (cm-3), TABS (μm), NETL (cm-3); and the following targets: JSC (mA/cm²), VOC (V), FF (%), η (%), and Δ50 (%).
