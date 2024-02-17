# Start from debian linux image (DockerHub)
FROM debian:bookworm-slim

# Add custom label
LABEL maintainer "christian Romero Garcia christian.romero@uvic.cat" \
      version "0.1" \
      description "Docker HandsOn R STDOUT script"

# Install R (after apt-get update)
RUN apt-get update && apt-get install -y r-base

# Install R package 'optparse'
RUN R -e 'install.packages("optparse", repos = "http://cloud.r-project.org/")'

RUN <<EOF
apt-get update
apt-get install -y curl
EOF

# Make the folder '/scripts' in the container
RUN mkdir /scripts

# Copy 'scripts/script.R' to the folder '/scripts' in the container
ADD scripts/script.R /scripts

# Give execution permissions to script.R
RUN chmod +x /scripts/script.R

# Add /scripts folder to the PATH environment variable
ENV PATH="$PATH:/scripts"

