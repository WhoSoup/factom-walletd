package main

import (
	"log"
	"net/http"
	_ "net/http/pprof"
)

// StartProfiler runs the go pprof tool
// `go tool pprof http://localhost:6063/debug/pprof/profile`
// https://golang.org/pkg/net/http/pprof/
func StartProfiler() {
	log.Println(http.ListenAndServe(":6063", nil))
	//runtime.SetBlockProfileRate(100000)
}
