The corpus of human scientific knowledge is incomprehensibly large and continues to expand. Even relatively narrow areas of research, such as high-performance computing (HPC) scheduling, contain thousands of peer-reviewed papers spanning decades of work. An expert in a field will generally know its foundational papers, major research directions, common methods, and current best practices. However, it is not realistic for any individual researcher to maintain a complete mental model of every relevant result, abandoned research direction, negative finding, assumption, or historical experiment.

This problem is particularly acute in software and HPC research. Many questions recur as systems, workloads, architectures, and software stacks change. A scheduling technique explored on vector supercomputers may become relevant again for heterogeneous accelerators. A limitation identified in an older batch scheduler may reappear in a modern distributed resource manager under a different name. Ideas developed independently in operating systems, cloud computing, workflow scheduling, distributed systems, machine learning systems, and HPC may address fundamentally similar problems while using entirely different terminology. As language and technology evolve, intellectual continuity becomes increasingly difficult to recognize.

Consequently, researchers may unknowingly rediscover existing ideas, repeat experiments whose important limitations are already known, or overlook older research directions that became dormant because the technological assumptions of the time made them impractical. Conversely, old conclusions can persist as conventional wisdom even when the systems on which those conclusions were based no longer resemble modern machines. Scientific progress therefore depends not only on finding recent papers, but on understanding how questions, assumptions, methods, and evidence have evolved across time.

Large language models have made this landscape substantially easier to navigate. Modern research assistants can summarize papers, search scientific literature, compare competing approaches, trace citations, and synthesize information across collections of documents. Tools such as Deep Research, NotebookLM, Semantic Scholar, Elicit, and PaperQA demonstrate that questions that once required days of exploratory literature review can increasingly be investigated interactively.

These capabilities begin to address the problem of scientific rediscovery by making a wider range of perspectives accessible to individual researchers. However, they introduce a second problem: the rate at which scientific information can be produced, consumed, and acted upon is increasing faster than the mechanisms researchers traditionally use to organize it.

The bottleneck is therefore beginning to move.

When reading papers was slow, a researcher could maintain much of the relevant state of a project in their own memory, laboratory notes, source repositories, and a modest collection of experimental results. LLM-assisted research changes this balance. A researcher can now explore substantially more literature, generate and evaluate more hypotheses, inspect unfamiliar software systems, modify research code quickly, and launch many more experimental branches than before. Agentic coding systems such as Claude Code and Codex make it possible to understand and modify unfamiliar research software at a rate that would previously have required significant manual effort.

This is especially consequential for software and HPC research, where scientific questions are often inseparable from complex software artifacts and experimental environments. A claim about a scheduler, runtime, communication library, simulator, or resource-management policy may depend on a particular source revision, compiler configuration, workload trace, machine topology, queue configuration, random seed, scheduler policy, or timing model. Reproducing or challenging the claim may therefore require reconstructing an entire experimental state rather than simply rerunning a script.

The ability to generate experiments faster does not remove this complexity. In many cases, it amplifies it.

A researcher may quickly create several implementations of an idea, dozens of configurations, hundreds of experiment runs, and multiple competing interpretations of their results. Without careful management, it becomes easy to forget why a particular experiment was run, which hypothesis it was intended to test, what software state produced it, whether an apparent anomaly was previously investigated, or how a result relates to a claim encountered months earlier in the literature. Agentic tools suffer from a similar problem: their effectiveness is constrained by the context that can be supplied to them. Giving an agent an entire project history, literature collection, source tree, and experimental archive is neither efficient nor necessarily useful.

The problem is therefore no longer simply how to generate more scientific work. It is how to maintain a coherent and trustworthy model of the rapidly expanding state of that work.

Shiroe is intended to address this problem.

Shiroe—named after the “castle of knowledge” associated with the protagonist of _Log Horizon_—is a research-management framework for coupling scientific knowledge across literature, research projects, and experiments. Rather than treating these as independent collections of papers, notes, repositories, and result files, Shiroe treats them as different layers of a continuously evolving research state.

The long-term goal of Shiroe is to help researchers understand what is known, what remains uncertain, how their own results change that understanding, and what work is most useful to perform next.

Shiroe is not intended to replace the researcher or autonomously conduct science. Its purpose is to preserve and expose the connections that researchers are increasingly expected to maintain mentally: between historical literature and modern systems, between claims and supporting evidence, between project hypotheses and experimental observations, and between unexpected results and unexplored research directions. Large language models provide the reasoning interface for navigating these connections, while explicit provenance and reproducibility information provide the grounding necessary to make that reasoning inspectable.

At the highest level, Shiroe operates across three coupled layers of knowledge: **literature, projects, and experiments**.

The literature layer represents the broader scientific landscape. It begins with a researcher-controlled corpus of relevant papers but is not limited to that corpus. External scholarly databases and literature-search systems can be used to discover related work, follow citations, explore historical terminology, and expand the corpus as new research questions emerge.

The purpose of this layer is not merely to store papers. Shiroe should help construct a model of the research represented by those papers: the questions researchers have asked, methods they have proposed, assumptions they have made, experimental evidence they have produced, limitations they have encountered, and disagreements that remain unresolved.

Importantly, this model must be temporal. A research question may be heavily studied for several years and then disappear. A technique may be abandoned because it was unsuitable for the hardware available at the time. An idea may later reappear under different terminology without citing the earlier body of work. Shiroe should make these trajectories visible so that researchers can distinguish genuinely new directions from rediscoveries and can identify dormant lines of inquiry that may be worth revisiting under modern technological conditions.

This is particularly valuable in HPC, where the underlying systems change dramatically over time while many high-level research problems remain recognizable. Questions involving resource allocation, backfilling, topology awareness, heterogeneity, workflow placement, runtime prediction, fairness, interference, and scheduler overhead may repeatedly acquire new relevance as machine architectures and workload characteristics change.

The second layer is the **project**.

A project represents a bounded research effort and acts as the interface between the global state of the literature and the local state of active research. Its exact scope is intentionally user-defined. A project may correspond to a broad research question, a new scheduling policy, a software tool, an optimization to an existing system, a reproducibility study, or an investigation of unexpected behavior in a production environment.

A project is therefore more than a directory containing source code.

It contains the evolving intellectual state of the work: the questions currently being investigated, hypotheses under consideration, claims believed to be relevant, assumptions that require verification, important design decisions, contradictions discovered during development, unresolved observations, and links to the literature that motivates or contextualizes them.

The literature layer informs this project state. When a researcher begins investigating a question, Shiroe should help identify relevant prior work, competing explanations, historically important results, and claims that may need to be independently verified. When the project produces a new observation, Shiroe should help relate that observation back to the literature: Does it support a known result? Contradict an assumption? Reproduce an older finding on a modern system? Suggest that a supposedly settled question should be reopened?

The relationship is therefore bidirectional. Literature informs the design of the project, while project results change how the literature should be interpreted.

The third layer is the **experiment**.

Experiments are where hypotheses become observations. Each experiment belongs to a project and records not only the data produced by an execution but the scientific reason the execution exists.

An experiment should preserve the question it was intended to answer, the hypothesis or decision that motivated it, the configuration under which it was performed, the provenance necessary to reproduce it, and a high-level interpretation of its results once they become available. In software and HPC research, this provenance may include source revisions, branches or patches, build options, dependency versions, compiler flags, input workloads, machine descriptions, scheduler configurations, environment variables, random seeds, job scripts, and other execution metadata.

The raw experimental data itself may live elsewhere. Shiroe's role is to maintain enough structured information to understand what that data means, where it came from, and how it relates to the scientific state of the project.

This distinction is important because modern research workflows can produce far more experimental data than either a human or an LLM can reasonably examine at once. The purpose of Shiroe is therefore not to continuously place every log file, result table, trace, and source file into an LLM context. Instead, each layer should maintain an information-management system that allows relevant evidence to be retrieved at the appropriate level of abstraction.

At the literature level, this may mean locating the handful of papers and passages relevant to a particular claim rather than presenting an agent with an entire library.

At the project level, it may mean retrieving the previous design decisions, hypotheses, failures, and experimental findings relevant to the current task rather than presenting the complete history of the project.

At the experiment level, it may mean surfacing the runs, parameters, anomalies, or derived results needed to evaluate a hypothesis rather than processing an entire result archive.

In this sense, Shiroe treats context as a resource that must itself be managed.

The three layers together form a feedback loop:

**Literature → Project → Experiment → Project → Literature**

The literature provides the current external state of knowledge. The project selects which uncertainties are locally important. Experiments produce evidence about those uncertainties. The resulting evidence modifies the project's understanding, which can then be compared against the broader literature to determine its significance and suggest new questions.

Eventually, Shiroe should be able to support questions such as:

- Which assumptions underlying this project have the weakest support in the literature?
    
- Has this research question been investigated previously under different terminology?
    
- Which older research directions disappeared without being conclusively resolved?
    
- Which published claims are important enough to this project that they should be independently reproduced?
    
- Which of our results contradict or qualify existing work?
    
- What experiments would best distinguish between the explanations currently supported by the evidence?
    
- Which experiment would reduce the greatest uncertainty in the current project?
    
- Have we already encountered this anomaly in an earlier branch or experiment?
    
- Does a new result make a previously abandoned research direction worth reconsidering?
    
- What evidence supports the statement we are preparing to make in a paper?
    

These are not fundamentally questions about files. They are questions about the state of scientific knowledge.

For this reason, Shiroe's central abstraction should not ultimately be papers, repositories, or experiment directories. Those objects contain evidence, but the intellectual structure of research consists of questions, claims, assumptions, hypotheses, methods, observations, contradictions, and conclusions.

A paper may provide evidence for a claim. A project may depend on that claim. An experiment may challenge it. A later experiment may explain the contradiction. A new literature search may reveal that a similar contradiction was observed twenty years earlier. Preserving these relationships allows the history of a project to remain useful rather than gradually disappearing into old notes, forgotten branches, and result directories.

This also creates an important distinction between different forms of knowledge. Shiroe should be able to distinguish direct observations from derived results, interpretations, and speculative hypotheses. The fact that an experiment produced a particular measurement is fundamentally different from an LLM's interpretation of why that measurement occurred. Likewise, an author's explicit statement in a paper is different from Shiroe inferring that several papers collectively represent an unresolved research gap.

Maintaining these distinctions is essential if LLMs are to participate meaningfully in scientific workflows. The system should not merely produce answers; it should preserve enough provenance to explain why those answers are believed.

Many individual tools already implement portions of this vision. Literature-management systems organize papers. Scientific search engines discover related work. Retrieval-augmented generation systems answer questions over document collections. Experiment trackers record runs and metrics. Workflow systems preserve execution information. Version-control systems record changes to software. Coding agents modify and reason about source code.

Shiroe does not need to replace these systems.

Instead, Shiroe should provide the connective layer between them.

Its purpose is to transform a collection of disconnected research artifacts into a persistent representation of a scientific investigation: what was believed, why it was believed, what was tested, what was observed, how that observation relates to prior work, and what question should be asked next.

As LLMs continue to increase the rate at which researchers can read literature, write software, explore hypotheses, and conduct experiments, the ability to preserve this research state may become as important as the ability to generate the work itself.

Shiroe is intended to make that state explicit, searchable, reproducible, and useful to both researchers and the agents working alongside them.