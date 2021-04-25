
subdir('src')

build_version_inc = configure_file(
    input : 'build-version.inc.in',
    output : 'build-version.inc',
    configuration : build_version_conf,
)

glslc_native = executable('glslc',
    glslc_src,
    dependencies : [shaderc_native_dep, shaderc_util_native_dep, glslang_native_dep, spirv_tools_native_dep],
    build_by_default : false,
    native : true,
    override_options : native_options,
)
