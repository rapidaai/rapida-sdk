package main

import (
	"context"

	"github.com/golang/protobuf/ptypes/any"
	rapida_definitions "github.com/rapidaai/rapida-sdk/rapida/definitions"
)

// Builder pattern for Invoke function parameters
type invokeRequestBuilder struct {
	endpoint rapida_definitions.EndpointDefinition
	ctx      context.Context
	inputs   map[string]*any.Any
	metadata map[string]*any.Any
	options  map[string]*any.Any
}

type RequestBuilder interface {
	WithContext(context.Context) RequestBuilder
}

func InvokeRequestBuilder(endpoint rapida_definitions.EndpointDefinition) RequestBuilder {
	return &invokeRequestBuilder{
		endpoint: endpoint,
		ctx:      context.Background(),
		inputs:   make(map[string]*any.Any),
		metadata: make(map[string]*any.Any),
		options:  make(map[string]*any.Any),
	}
}

// WithInputs sets the inputs parameter
func (b *invokeRequestBuilder) WithContext(ctx context.Context) RequestBuilder {
	b.ctx = ctx
	return b
}

// WithInputs sets the inputs parameter
func (b *invokeRequestBuilder) WithInputs(inputs map[string]*any.Any) *invokeRequestBuilder {
	b.inputs = inputs
	return b
}

// WithMetadata sets the metadata parameter
func (b *invokeRequestBuilder) WithMetadata(metadata map[string]*any.Any) *invokeRequestBuilder {
	b.metadata = metadata
	return b
}

// WithOptions sets the options parameter
func (b *invokeRequestBuilder) WithOptions(options map[string]*any.Any) *invokeRequestBuilder {
	b.options = options
	return b
}

// Build returns the parameters needed for the Invoke function
func (b *invokeRequestBuilder) Build() (rapida_definitions.EndpointDefinition, map[string]*any.Any, map[string]*any.Any, map[string]*any.Any) {
	return b.endpoint, b.inputs, b.metadata, b.options
}
