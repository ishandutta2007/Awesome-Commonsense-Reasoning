import re

with open(r'C:\Users\ishan\Documents\Projects\Awesome-Commonsense-Reasoning\README.md', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '**The Symbolic Rule & Fact Axiom Era (Cyc / GOFAI Baseline, ~1984–1990s)**': '[**The Symbolic Rule & Fact Axiom Era (Cyc / GOFAI Baseline, ~1984–1990s)**](docs/symbolic_rule_and_fact_axiom_era.md)',
    '**The Crowdsourced Semantic Knowledge Graph Era (ConceptNet / ATOMIC, ~2000s–2019)**': '[**The Crowdsourced Semantic Knowledge Graph Era (ConceptNet / ATOMIC, ~2000s–2019)**](docs/crowdsourced_semantic_knowledge_graph_era.md)',
    '**The Statistical LLM Associative Era (GPT-3 / GPT-4, ~2020–2023)**': '[**The Statistical LLM Associative Era (GPT-3 / GPT-4, ~2020–2023)**](docs/statistical_llm_associative_era.md)',
    '**The Native Reinforcement-Learned Search & Verification Era (~2024–Present)**': '[**The Native Reinforcement-Learned Search & Verification Era (~2024–Present)**](docs/native_rl_search_and_verification_era.md)',
    '**A. Physical Commonsense (Spatiotemporal Dynamics)**': '[**A. Physical Commonsense (Spatiotemporal Dynamics)**](docs/physical_commonsense.md)',
    '**B. Social & Psychological Commonsense (Theory of Mind)**': '[**B. Social & Psychological Commonsense (Theory of Mind)**](docs/social_psychological_commonsense.md)',
    '**C. Abductive Reasoning (Cause-and-Effect Inversion)**': '[**C. Abductive Reasoning (Cause-and-Effect Inversion)**](docs/abductive_reasoning.md)',
    '**D. Qualitative / Counterfactual Reasoning**': '[**D. Qualitative / Counterfactual Reasoning**](docs/qualitative_counterfactual_reasoning.md)',
    '**Generative World Simulators (Video Diffusion Transformers)**': '[**Generative World Simulators (Video Diffusion Transformers)**](docs/generative_world_simulators.md)',
    '**Process-Supervised Step Verifiers (PRMs)**': '[**Process-Supervised Step Verifiers (PRMs)**](docs/process_supervised_step_verifiers.md)',
    '**The Contamination and Dataset Saturation Trap**': '[**The Contamination and Dataset Saturation Trap**](docs/contamination_and_dataset_saturation_trap.md)',
    '**The Polysemantic Neuron Superposition Challenge**': '[**The Polysemantic Neuron Superposition Challenge**](docs/polysemantic_neuron_superposition_challenge.md)',
    '**Multi-Task Autonomous Humanoid Fleets & Factory Logistics**': '[**Multi-Task Autonomous Humanoid Fleets & Factory Logistics**](docs/multi_task_autonomous_humanoid_fleets.md)',
    '**Autonomous Vehicle Perception & Defensives Navigation Stacks**': '[**Autonomous Vehicle Perception & Defensives Navigation Stacks**](docs/autonomous_vehicle_perception.md)',
    '**Enterprise Multi-Agent Corporate Orchestration & Task Execution**': '[**Enterprise Multi-Agent Corporate Orchestration & Task Execution**](docs/enterprise_multi_agent_corporate_orchestration.md)'
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(r'C:\Users\ishan\Documents\Projects\Awesome-Commonsense-Reasoning\README.md', 'w', encoding='utf-8') as f:
    f.write(content)
