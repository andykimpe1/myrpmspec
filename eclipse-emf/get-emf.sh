#!/bin/sh

rm -rf org.eclipse.emf
rm -rf org.eclipse.mdt
rm -rf emf-2.6.0

cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.all-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.codegen.ecore-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.codegen.ecore.ui-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.codegen-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.codegen.ui-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.common-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.common.ui-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.converter-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.databinding.edit-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.databinding-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.ecore.edit-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.ecore.editor-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.ecore-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.edit-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.edit.ui-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.mapping.ecore.editor-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.mapping.ecore-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.mapping-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.mapping.ui-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/features/org.eclipse.emf.sdk-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.ant
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.codegen
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.codegen.ecore
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.codegen.ecore.ui
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.codegen.ui
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.common
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.common.ui
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.converter
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.databinding
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.databinding.edit
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.ecore
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.ecore.change
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.ecore.change.edit
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.ecore.edit
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.ecore.editor
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.ecore.xmi
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.edit
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.edit.ui
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.example.installer
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.exporter
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.importer
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.importer.ecore
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.importer.java
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.importer.rose
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.mapping
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.mapping.ecore
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.mapping.ecore2ecore
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.mapping.ecore2ecore.editor
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.mapping.ecore2xml
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.mapping.ecore2xml.ui
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.mapping.ecore.editor
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/plugins/org.eclipse.emf.mapping.ui
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.activities
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.examples
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.examples.databinding.project.core
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.examples.databinding.project.core.model
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.examples.databinding.project.ui.rcp
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.examples-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.examples.generator.validator
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.examples.library
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.examples.library.edit
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.examples.library.editor
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.exporter.html
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.java
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.java.edit
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/examples/org.eclipse.emf.java.editor
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.test.build
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.test.common
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.test.core
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.test.databinding
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.test.databinding.edit
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.test.edit
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.test.examples
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.test.performance
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.tests
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.test.sdo
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.tests-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.test.tools
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/tests/org.eclipse.emf.test.xml
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/doc/org.eclipse.emf.cheatsheets
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/doc/org.eclipse.emf.doc
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/doc/org.eclipse.emf.doc-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/doc/org.eclipse.emf.examples.jet.article2
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.emf/org.eclipse.emf/releng/org.eclipse.emf.build-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/features/org.eclipse.xsd.ecore.converter-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/features/org.eclipse.xsd.edit-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/features/org.eclipse.xsd.editor-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/features/org.eclipse.xsd.example-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/features/org.eclipse.xsd-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/features/org.eclipse.xsd.mapping.editor-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/features/org.eclipse.xsd.mapping-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/features/org.eclipse.xsd.sdk-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/plugins/org.eclipse.emf.mapping.xsd2ecore
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/plugins/org.eclipse.emf.mapping.xsd2ecore.editor
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/plugins/org.eclipse.xsd
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/plugins/org.eclipse.xsd.ecore.converter
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/plugins/org.eclipse.xsd.ecore.exporter
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/plugins/org.eclipse.xsd.ecore.importer
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/plugins/org.eclipse.xsd.edit
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/plugins/org.eclipse.xsd.editor
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/plugins/org.eclipse.xsd.example.installer
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/plugins/org.eclipse.xsd.mapping
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/plugins/org.eclipse.xsd.mapping.editor
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/plugins/org.eclipse.xsd.test
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/doc/org.eclipse.xsd.cheatsheets
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/doc/org.eclipse.xsd.doc
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/doc/org.eclipse.xsd.doc-feature
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/modeling export -r R2_6_0 org.eclipse.mdt/org.eclipse.xsd/examples/org.eclipse.xsd.example
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/eclipse export -r v20100118 org.eclipse.test
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/eclipse export -r v20080717 org.eclipse.ant.optional.junit

mkdir emf-2.6.0
mv org.eclipse.emf/org.eclipse.emf/{doc,examples,features,plugins,releng,tests}/* emf-2.6.0/
mv org.eclipse.mdt/org.eclipse.xsd/{doc,examples,features,plugins}/* emf-2.6.0/
mv org.eclipse.test emf-2.6.0/
mv org.eclipse.ant.optional.junit emf-2.6.0/
tar cjf emf-2.6.0.tar.gz emf-2.6.0

rm -rf org.eclipse.emf
rm -rf org.eclipse.mdt
