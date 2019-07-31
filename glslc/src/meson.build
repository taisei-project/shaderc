
glslc_src = files(
    'dependency_info.cc',
    'file.cc',
    'file_compiler.cc',
    'file_includer.cc',
    'main.cc',
    'resource_parse.cc',
    'shader_stage.cc',
)

build_version_conf = configuration_data()
build_version_conf.set('SHADERC_VERSION', meson.project_version())
build_version_conf.set('SPVTOOLS_VERSION', spirv_tools_native_dep.version())
build_version_conf.set('GLSLANG_VERSION', glslang_native_dep.version())
