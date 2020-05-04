
subdir('src')
subdir('include')

libshaderc_util = static_library('shaderc_util',
    shaderc_util_src,
    dependencies : [glslang_dep, spirv_tools_dep],
    include_directories : shaderc_util_incdirs,
    build_by_default : false,
)

shaderc_util_dep = declare_dependency(
    link_with : libshaderc_util,
    include_directories : shaderc_util_incdirs,
    version : meson.project_version(),
)

libshaderc_util_native = static_library('shaderc_util_native',
    shaderc_util_src,
    dependencies : [glslang_native_dep, spirv_tools_native_dep],
    include_directories : shaderc_util_incdirs,
    build_by_default : false,
    native : true,
    override_options : native_options,
)

shaderc_util_native_dep = declare_dependency(
    link_with : libshaderc_util_native,
    include_directories : shaderc_util_incdirs,
    version : meson.project_version(),
)
