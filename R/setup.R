# Load Packages
suppressPackageStartupMessages(library(tidyverse))
library(knitr)

# Set up global variables
data_dir <- file.path("..", "data")

# Team light!
theme_set(theme_light())

load_datasets <- function(include_variants = FALSE) {
  datasets <- read_csv(
    file.path(data_dir, "raw", "annotated_datasets.csv")
  )

  if (!include_variants) {
    datasets <- datasets %>%
      # Keep only one row per "dataset"
      distinct(dataset_id, .keep_all = TRUE)
  }

  return(datasets)
}

load_papers <- function() {
  papers <- read_csv(
    file.path(data_dir, "raw", "annotated_papers-x-datasets.csv")
  )

  return(papers)
}

load_papers_2023 <- function() {
  papers_2023 <- read_csv(
    file.path(data_dir, "raw", "annotated_papers-2023.csv")
  )

  return(papers_2023)
}

# Helper to output nice tables
show <- function(x) {
  if (isTRUE(getOption('knitr.in.progress'))) {
    return(kable(x))
  } else {
    return(print(x))
  }
}

# Mapping Quality Checker
check_mapping_quality <- function (
  mapping,
  target_ref,
  standard_ref = standard_labels
) {
  colname_target <- intersect(colnames(mapping), colnames(target_ref))
  colname_ref <- intersect(colnames(mapping), colnames(standard_ref))

  if ((length(colname_target) + length(colname_ref)) != 2) {
    warning("No clear mapping columns")
  }
  if (colname_ref != "sensitive_standard") {
    stop("Second reference should be the standard labels")
  }

  missing_standard_labels <- setdiff(
    standard_ref[[colname_ref]],
    mapping[[colname_ref]]
  )
  if (length(missing_standard_labels) > 0) {
    print(missing_standard_labels)
    stop("Error in mapping: Missing standard labels in mapping.")
  }
  extra_standard_labels <- setdiff(
    mapping[[colname_ref]],
    standard_ref[[colname_ref]]
  )
  if (length(extra_standard_labels) > 0) {
    print(extra_standard_labels)
    stop("Error in mapping: Extra standard labels in mapping.")
  }

  extra_mapped_labels <- setdiff(
    mapping[[colname_target]],
    target_ref[[colname_target]]
  ) |> na.omit()
  if (length(extra_mapped_labels) > 0) {
    print(extra_mapped_labels)
    stop("Error in mapping: Extra target labels in mapping (i.e. the not-standard side of the mapping).")
  }
  missing_mapped_labels <- setdiff(
    target_ref[[colname_target]],
    mapping[[colname_target]]
  )
  if (length(missing_mapped_labels) > 0) {
    print(missing_mapped_labels)
    message(
      paste(
        "Note: Missing target labels in mapping.",
        "This means not everything on the target site is mapped onto,",
        " but may be ok."
      )
    )
  }
}
