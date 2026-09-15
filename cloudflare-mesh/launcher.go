package main

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"
	"syscall"
)

type options struct {
	MeshNodeToken string `json:"mesh_node_token"`
	SrcnatEnabled bool   `json:"srcnat_enabled"`
}

func main() {
	config, err := readOptions()
	if err != nil {
		fatal("Unable to read Home Assistant app configuration: %v", err)
	}

	if strings.TrimSpace(config.MeshNodeToken) == "" {
		fatal("mesh_node_token must be configured before the app can start")
	}



	setEnvironment("MESH_NODE_TOKEN", config.MeshNodeToken)
	setEnvironment("SRCNAT_ENABLED", fmt.Sprintf("%t", config.SrcnatEnabled))

	fmt.Println("[INFO] Starting Cloudflare Mesh")
	if err := syscall.Exec("/entrypoint", []string{"/entrypoint"}, os.Environ()); err != nil {
		fatal("Unable to start the Cloudflare Mesh entrypoint: %v", err)
	}
}

func readOptions() (options, error) {
	var config options
	contents, err := os.ReadFile("/var/lib/cloudflare-warp/options.json")
	if err != nil {
		return config, fmt.Errorf("failed to read /var/lib/cloudflare-warp/options.json: %w", err)
	}
	if err := json.Unmarshal(contents, &config); err != nil {
		return config, fmt.Errorf("failed to parse JSON: %w", err)
	}
	return config, nil
}



func setEnvironment(key, value string) {
	if err := os.Setenv(key, value); err != nil {
		fatal("Unable to set %s: %v", key, err)
	}
}

func fatal(format string, args ...any) {
	fmt.Fprintf(os.Stderr, "[ERROR] "+format+"\n", args...)
	os.Exit(1)
}
