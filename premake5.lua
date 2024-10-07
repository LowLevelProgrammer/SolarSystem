workspace "SolarSystem"
    architecture "x64"

    configurations
    {
        "Debug",
        "Release",
        "Dist"
    }

    cppdialect "C++17"

    outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

    project "SolarSystem"
        location "SolarSystem"
        kind "ConsoleApp"
        language "C++"

        targetdir ("bin/" .. outputdir .. "/%{prj.name}")
        objdir ("bin-int/" .. outputdir .. "/{prj.name}")

        -- Source files
        files
        {
            "%{prj.name}/src/**.h",
            "%{prj.name}/src/**.cpp",
        }

        Vendor = "%{prj.name}/vendor/"

        -- Vendor source files
        files
        {
            (Vendor .. "glad/src/**.c")
        }

        includedirs
        {
            (Vendor .. "GLFW/include"),
            (Vendor .. "glad/include")
        }

    filter "system:windows"
        libdirs
        {
            (Vendor .. "GLFW/lib-vc2022"),
        }

    links
    {
        "opengl32",
        "glfw3"
    }
    
    filter "configurations:Debug"
        symbols "On"

    filter "configurations:Release"
        optimize "On"

    filter "configurations:Dist"
        optimize "On"
