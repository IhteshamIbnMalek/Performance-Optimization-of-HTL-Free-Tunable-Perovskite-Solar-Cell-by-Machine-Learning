# Performance-Optimization-of-HTL-Free-Tunable-Perovskite-Solar-Cell-by-Machine-Learning
Machine learning is used to optimize HTL-free perovskite solar cells by tuning fabrication parameters. SCAPS-1D simulations generated 1,650 samples to train models that accurately predict performance, enabling stable and cost-effective designs.

1. PSC_HTL_free_opt_model.def contains the SCAPS parameters used for the optimized case. These parameters can be modified as needed.

2. HTL_free_batch_setup.sbf contains the SCAPS batch setup parameters (features) used to generate the dataset, excluding degradation. Degradation values can be obtained by varying the defect density over time.

3. HTL_free_recorder_setup.srf includes the SCAPS recorder setup parameters (targets) used to record the corresponding performance metrics.

4. Trained_4_degree_Polynomial_Regressor.pkl contains the trained 4th-degree polynomial regressor model. Upload this file to the session storage in Google Colab. Then, use the script PR4_model_prediction.py to predict the target values for efficiency and degradation.

5. Trained_MLP_Classifier.h5 contains the trained multilayer perceptron (MLP) classifier, which can similarly be used to determine whether given fabrication parameters lead to superior performance.

6. PSC_HTL_free_Dataset_IIM.xlsx contains the dataset of 1650 samples, with the following features: x (%), NABS (cm-3), TABS (μm), NETL (cm-3); and the following targets: JSC (mA/cm²), VOC (V), FF (%), η (%), and Δ50 (%).

Citing our work:
If you use our generated data and/or find the code useful, cite our preprint: 
 
Ihtesham Ibn Malek, Hafiz Imtiaz, and Samia Subrina. “Simultaneous Optimization of Efficiency and Degradation in Tunable HTL-Free Perovskite Solar Cells with MWCNT-Integrated Back Contact Using a Machine Learning-Derived Polynomial Regressor.” (2025), DOI: https://doi.org/10.48550/arXiv.2505.18693.
 
BibTex:
 
@misc{malek2025simultaneouso,
      title={Simultaneous Optimization of Efficiency and Degradation in Tunable HTL-Free Perovskite Solar Cells with MWCNT-Integrated Back Contact Using a Machine Learning-Derived Polynomial Regressor}, 
      author={Ihtesham Ibn Malek and Hafiz Imtiaz and Samia Subrina},
      year={2025},
      eprint={2505.18693},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2505.18693}, 
}
