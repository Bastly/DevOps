
# Create a atahulpa
resource "openstack_compute_instance_v2" "atahualpa1" {
  name = "atahualpa1"
  image_id = "bb02b1a3-bc77-4d17-ab5b-421d89850fca"
  flavor_id = "general1-1"
  region = "IAD"
  metadata {
    type = "atahualpa"
  }
  key_pair = "openstack"
}


# Create a chaski1
resource "openstack_compute_instance_v2" "chaski1" {
  name = "chaski1"
  image_id = "bb02b1a3-bc77-4d17-ab5b-421d89850fca"
  flavor_id = "general1-1"
  region = "IAD"
  metadata {
    type = "chaski"
  }
  key_pair = "openstack"
}


# Create a chaski2
resource "openstack_compute_instance_v2" "chaski2" {
  name = "chaski2"
  image_id = "bb02b1a3-bc77-4d17-ab5b-421d89850fca"
  flavor_id = "general1-1"
  region = "IAD"
  metadata {
    type = "chaski"
  }
  key_pair = "openstack"
}


# Create a consul server
resource "openstack_compute_instance_v2" "consul1" {
  name = "consul1"
  image_id = "bb02b1a3-bc77-4d17-ab5b-421d89850fca"
  flavor_id = "general1-1"
  region = "IAD"
  metadata {
    type = "consulServer"
  }
  key_pair = "openstack"
}

# Create a orion
resource "openstack_compute_instance_v2" "orion1" {
  name = "orion1"
  image_id = "592c879e-f37d-43e6-8b54-8c2d97cf04d4"
  flavor_id = "general1-1"
  region = "IAD"
  metadata {
    type = "orion"
  }
  key_pair = "openstack"
}

# Create a connector-rest
resource "openstack_compute_instance_v2" "connector1" {
  name = "connector1"
  image_id = "bb02b1a3-bc77-4d17-ab5b-421d89850fca"
  flavor_id = "general1-1"
  region = "IAD"
  metadata {
    type = "connectorrest"
  }
  key_pair = "openstack"
}

# Create a elk
resource "openstack_compute_instance_v2" "elk1" {
  name = "elk1"
  image_id = "bb02b1a3-bc77-4d17-ab5b-421d89850fca"
  flavor_id = "general1-1"
  region = "IAD"
  metadata {
    type = "elk"
  }
  key_pair = "openstack"
}
