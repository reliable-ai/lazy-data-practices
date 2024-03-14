qmd_files <- list.files(path = "notebooks", pattern = "\\.qmd$", full.names = TRUE)

# Render each .qmd file
for(file in qmd_files) {
  quarto::quarto_render(file, output_format = "html")
}
