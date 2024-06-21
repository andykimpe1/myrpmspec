/* LD_PRELOAD library used as a workaround for RHBZ#563103 & RHBZ#968905. */

#define _GNU_SOURCE 1
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <dlfcn.h>

ssize_t
preadv (int fd, ...)
{
  errno = ENOSYS;
  return -1;
}

ssize_t
preadv64 (int fd, ...)
{
  errno = ENOSYS;
  return -1;
}

ssize_t
pwritev(int fd, ...)
{
  errno = ENOSYS;
  return -1;
}

ssize_t
pwritev64 (int fd, ...)
{
  errno = ENOSYS;
  return -1;
}

static int (*orig_socket) (int domain, int type, int protocol);

int
socket (int domain, int type, int protocol)
{
  /* Remove SOCK_CLOEXEC flag. */
  return orig_socket (domain, type & ~02000000, protocol);
}

static void init (void) __attribute__((constructor));

static void
init (void)
{
  orig_socket = dlsym (RTLD_NEXT, "socket");
}
