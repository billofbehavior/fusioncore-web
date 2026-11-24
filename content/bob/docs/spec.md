---
title: "SBOB specification"
description: "Version 0.3.1 in brief: what the Software Bill of Behavior specifies, chapter by chapter."
weight: 20
type: "docs"
draft: false
---

<div class="spec-status">
  <div><span>Version</span><strong>0.3.1</strong></div>
  <div><span>Stage</span><strong>Draft proposal, work in progress</strong></div>
  <div><span>Updated</span><strong>22 November 2026</strong></div>
  <div><span>Full text</span><strong><a href="https://github.com/k8sstormcenter/sbob-spec/blob/main/spec/sbob-v0.3.1.md">sbob-v0.3.1.md</a></strong></div>
</div>

This page summarizes the specification for reading on the web. The full text, with numbered clauses, schemas and the registry of names, lives in [k8sstormcenter/sbob-spec](https://github.com/k8sstormcenter/sbob-spec). Where this summary and the full text differ, the full text is right.

Nothing here is settled. The specification is written in the open so that the people who build runtime-security tools can tell us where it is wrong, where it is unnecessary and where it gets in their way.

## In one paragraph

An SBOB is a declarative document that states what a piece of software is **intended to do at run time**: which programs it starts and with which arguments, which files it opens, which system calls and Linux capabilities it uses, which HTTP endpoints it serves or calls, and which network peers it accepts or contacts. A verifier compares what it observes with the document and reports what the document does not admit. The specification is independent of any implementation.

| artifact | what it covers | relation to an SBOB |
|---|---|---|
| SBOM | packages, versions, licences | complementary |
| VEX statement | whether a known vulnerability is exploitable | complementary |
| seccomp or AppArmor profile | kernel-enforced system-call and resource policy | adjacent; an SBOB may carry a seccomp profile |

## What a document looks like

An illustrative document: the workload may run `curl`, but never with `--insecure`, may read its configuration, and is intended to open no outbound connections at all.

```yaml
apiVersion: profiles.sbob/v1beta1
kind: RuntimeProfile
subject: container
metadata:
  name: web
  annotations:
    # written by a person, so it may govern a workload
    sbob/managed-by: User
    sbob/spec-version: "0.3.1"
spec:
  architectures: [amd64]
  capabilities: [CAP_NET_BIND_SERVICE]
  execs:
  - {path: /usr/bin/curl, args: [curl, ⋯⋯]}
  opens:
  - {path: /etc/nginx/⋯⋯, flags: [O_RDONLY]}
  # present and empty: no outbound peers intended
  egress: []
  subtract:
    execs:
    - {path: /usr/bin/curl, args: [curl, --insecure, ⋯⋯]}
```

`⋯` stands for exactly one path segment or argument, `⋯⋯` for a run of them. An observation is admitted when an allow entry matches it and no subtract entry does.

## The chapters

<div class="spec-chapters">

<section class="spec-ch">
<p class="spec-ch__head"><span class="spec-ch__no">0</span><span class="spec-ch__stage">Normative</span></p>
<h3>Introduction and conformance</h3>
<p>Terms, and the difference between an absent section and an explicitly empty one. Five conformance classes, each tied to chapters: document producer, matcher, composer, verifier and rule engine. An implementation names the classes it claims and the version it conforms to.</p>
<a href="https://github.com/k8sstormcenter/sbob-spec/blob/main/spec/00-introduction-and-conformance.md">Chapter 0 →</a>
</section>

<section class="spec-ch">
<p class="spec-ch__head"><span class="spec-ch__no">1</span><span class="spec-ch__stage">Normative</span></p>
<h3>The behavior document</h3>
<p>One kind, <code>RuntimeProfile</code>, describes a container, the containers of one workload, or a host. Only a document marked as written by a person can govern a workload; a learned document never does. Kubescape's existing <code>ContainerProfile</code> form stays readable and converts back without loss.</p>
<a href="https://github.com/k8sstormcenter/sbob-spec/blob/main/spec/01-document.md">Chapter 1 →</a>
</section>

<section class="spec-ch">
<p class="spec-ch__head"><span class="spec-ch__no">2</span><span class="spec-ch__stage">Normative</span></p>
<h3>Pattern and matching grammar</h3>
<p>How paths, argument lists, executable names, IP addresses and CIDR blocks, DNS names, ports and protocols are matched, and how the allow and subtract sections are evaluated together. It also defines which entries can never match, so a validator can reject them.</p>
<a href="https://github.com/k8sstormcenter/sbob-spec/blob/main/spec/02-grammar.md">Chapter 2 →</a>
</section>

<section class="spec-ch">
<p class="spec-ch__head"><span class="spec-ch__no">3</span><span class="spec-ch__stage">Normative</span></p>
<h3>Collapse of learned documents</h3>
<p>A learned document records literal paths, arguments and endpoints. Collapse generalizes them into patterns, so the same behavior with different process numbers, counters, per-request directories or script names is still admitted. Collapsing the programs a second time gives the same result as collapsing them once.</p>
<a href="https://github.com/k8sstormcenter/sbob-spec/blob/main/spec/03-collapse.md">Chapter 3 →</a>
</section>

<section class="spec-ch">
<p class="spec-ch__head"><span class="spec-ch__no">4</span><span class="spec-ch__stage">Normative</span></p>
<h3>Composition of fragments</h3>
<p>The document that governs a workload can come in fragments: a base written with the software, an admission fragment added where it is deployed, overlays added later. A subtract entry wins in whichever fragment it is written. The chapter also defines the residual: what was observed but is not admitted, which tooling uses to propose additions.</p>
<a href="https://github.com/k8sstormcenter/sbob-spec/blob/main/spec/04-compose.md">Chapter 4 →</a>
</section>

<section class="spec-ch">
<p class="spec-ch__head"><span class="spec-ch__no">5</span><span class="spec-ch__stage spec-ch__stage--draft">Draft</span></p>
<h3>Trust</h3>
<p>Fragments written and signed by different parties. A bundle manifest, signed fragments, the verdicts a verifier reports, and the inputs of a trust policy that decides which fragments are accepted.</p>
<a href="https://github.com/k8sstormcenter/sbob-spec/blob/main/spec/05-trust.md">Chapter 5 →</a>
</section>

<section class="spec-ch">
<p class="spec-ch__head"><span class="spec-ch__no">6</span><span class="spec-ch__stage">Normative</span></p>
<h3>Rules</h3>
<p>The rule model in the Common Expression Language (CEL), the event fields a rule sees, and the profile functions through which a rule asks whether the document admits an observation. Also a catalogue of generalized rule names, rule policies, tags, bindings and the reporting of lost events.</p>
<a href="https://github.com/k8sstormcenter/sbob-spec/blob/main/spec/06-rules.md">Chapter 6 →</a>
</section>

<section class="spec-ch">
<p class="spec-ch__head"><span class="spec-ch__no">7</span><span class="spec-ch__stage">Normative</span></p>
<h3>Portability to other engines</h3>
<p>Other engines (another rule engine, an admission controller, a system-call filter) cannot run the CEL rules directly. Instead of translating rules, each engine would receive the expected behavior as data in its own form. Every rule of the reference set is given a fidelity class.</p>
<a href="https://github.com/k8sstormcenter/sbob-spec/blob/main/spec/07-portability.md">Chapter 7 →</a>
</section>

<section class="spec-ch">
<p class="spec-ch__head"><span class="spec-ch__no">8</span><span class="spec-ch__stage spec-ch__stage--draft">Draft</span></p>
<h3>Wire-level intent</h3>
<p>Optional <code>extensions</code> on endpoint and network entries state what is intended on the wire: the application protocol, the peer, the transport security, and the classes of data that may travel. An engine that ignores them matches exactly as before.</p>
<a href="https://github.com/k8sstormcenter/sbob-spec/blob/main/spec/08-wire-intent.md">Chapter 8 →</a>
</section>

<section class="spec-ch">
<p class="spec-ch__head"><span class="spec-ch__no">A</span><span class="spec-ch__stage">Normative</span></p>
<h3>Regular-expression rendering</h3>
<p>For engines that evaluate regular expressions instead of the matcher: how a path or argument pattern is rendered to one RE2 expression, and when a rendering conforms.</p>
<a href="https://github.com/k8sstormcenter/sbob-spec/blob/main/spec/appendix-a-regex.md">Appendix A →</a>
</section>

</div>

## Where it is being tried out

| chapter | where it is being tried out |
|---|---|
| 1 Document | [sbob-go](https://github.com/k8sstormcenter/sbob-go), the reference library, and a fork of the Kubescape storage |
| 2 Grammar | sbob-go and a fork of the Kubescape node-agent |
| 3 Collapse | sbob-go, the forked storage and [bobctl](https://github.com/k8sstormcenter/bob) |
| 4 Compose | sbob-go and the forked node-agent |
| 5 Trust | the forked node-agent and bobctl |
| 6 Rules | the rule set of the forked node-agent |
| 7 and appendix A | not tried yet; questions for the maintainers of Falco, Tetragon and Kubewarden |

These experiments test whether the ideas hold together. They are not a product.

## What changed since 0.0.4

- One kind, `RuntimeProfile`, with a `subject` field replaces `ContainerProfile`. Labels and annotations use the prefix `sbob/`.
- A subtract section lists what stays denied, whatever the allow sections say.
- Collapse, composition of fragments and trust are new chapters.
- Two conformance targets became five classes, each tied to chapters.
- The comparison of four tools in unverified columns is gone. Portability is now stated per rule, as a fidelity class.

The text of [version 0.0.4](https://github.com/k8sstormcenter/sbob-spec/blob/main/spec/sbob-v0.0.4.md) is kept unchanged as the starting point.

## Roadmap

Alignment with OpenTelemetry is a goal. Today the rules use the event fields and rule identifiers of the Kubescape node-agent. We would like them to become semantic rules, named in the terms of the OpenTelemetry semantic conventions, so that every tool could report the same behavior under the same name. That chapter is not started yet; first the schema of the document itself has to settle.

## Feedback

Comments, objections and corrections are very welcome, especially from people who maintain runtime-security and observability tools. If the draft misdescribes your project, tell us: we would rather change the draft than ask anyone to change their tool.

- Open an issue on [sbob-spec](https://github.com/k8sstormcenter/sbob-spec/issues).
- Talk to us in **#sbob-bill-of-behavior** on the [CNCF Slack](https://slack.cncf.io).
